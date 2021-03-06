import unittest

from habitica_api.user import User
from habitica_api import task
from habitica_api import API
from habitica_api.daily import Daily, Dailys
from habitica_api.habit import Habit, Habits
from habitica_api.todo import ToDo, ToDos
from habitica_api.tag import Tag, Tags
from habitica_api import Inventory

API.BASE_URL = "http://localhost:3000/api/v3/"

loginfile = open('test_credentials')
username = loginfile.readline().strip()
password = loginfile.readline().strip()
loginfile.close()


class TestAPILogin(unittest.TestCase):

    def test_login(self):
        auth = API.Authentication
        auth.login(username, password)
        self.assertTrue(auth.logged_in)


class TestUserProfile(unittest.TestCase):

    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)
        self.user = User()

    def test_status_update(self):
        self.user.update_status()
        self.assertIsNotNone(self.user.hp)
        self.assertIsNotNone(self.user.maxhp)
        self.assertIsNotNone(self.user.mp)
        self.assertIsNotNone(self.user.maxmp)
        self.assertIsNotNone(self.user.xp)
        self.assertIsNotNone(self.user.xp_to_level)
        self.assertIsNotNone(self.user.gp)


class TestHabits(unittest.TestCase):

    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)
        self.user = User()

    def test_read_habits(self):
        test_task_name = "Test habit"
        self.assertIn(test_task_name, [habit.text for habit in Habits()])

    def test_add_habit(self):
        test_values = {}
        test_values['text'] = "Test creation habit"
        test_values['notes'] = "Test habit notes"
        test_values['up'] = True
        test_values['down'] = False
        test_values['priority'] = 1.5

        habit = Habit.new(**test_values)
        self.assertIn(habit.id, [h.id for h in Habits()])
        self.assertEqual(habit.text, test_values['text'])
        self.assertEqual(habit.notes, test_values['notes'],
                         'Notes do not match')
        self.assertEqual(habit.up, test_values['up'], 'Up is set to false')
        self.assertEqual(habit.down, test_values['down'],
                         'Down is set to true')
        self.assertEqual(habit.priority, test_values['priority'],
                         'Difficulty does not match')
        habit.delete()

    def test_delete_habit(self):
        habit = Habit.new(text='Test deletion habit')
        habit.delete()
        self.assertNotIn(habit.id, [h.id for h in Habits()])

    def test_edit_habit(self):
        test_values = {}
        test_values['text'] = "Test modification habit"
        test_values['notes'] = "Test habit notes"
        test_values['up'] = True
        test_values['down'] = False
        test_values['priority'] = 1.5
        habit = Habit.new(**test_values)
        edited_task = {}
        edited_task['text'] = "Test modified habit"
        edited_task['notes'] = "Modified notes"
        edited_task['up'] = False
        edited_task['down'] = True
        edited_task['priority'] = 0.1
        habit.modify(edited_task)
        self.assertNotEqual(test_values['text'], habit.text)
        self.assertEqual(edited_task['text'], habit.text)
        self.assertEqual(habit.notes, edited_task['notes'])
        self.assertEqual(habit.up, edited_task['up'])
        self.assertEqual(habit.down, edited_task['down'])
        self.assertEqual(habit.priority, edited_task['priority'])
        habit.delete()


class TestDailys(unittest.TestCase):
    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_read_dailies(self):
        test_task_name = "Test daily"
        self.assertIn(test_task_name, [daily.text for daily in Dailys()])

    def test_add_daily(self):
        test_values = {}
        test_values['text'] = "Test creation daily"
        test_values['notes'] = "Test daily notes"
        test_values['priority'] = 2
        test_values['repeat'] = {
            'su': True,
            'm': False,
            't': True,
            'w': False,
            'th': True,
            'f': False,
            's': True
        }
        test_values['frequency'] = 'weekly'

        daily = Daily.new(**test_values)
        self.assertIn(daily.id, [d.id for d in Dailys()])
        self.assertEqual(daily.text, test_values['text'])
        self.assertEqual(daily.notes, test_values['notes'])
        self.assertEqual(daily.priority, test_values['priority'])
        self.assertEqual(daily.repeat, test_values['repeat'])
        self.assertEqual(daily.frequency, test_values['frequency'])
        daily.delete()

    def test_add_xdays_daily(self):
        test_values = {}
        test_values['text'] = "Test xdays daily"
        test_values['everyX'] = 5
        test_values['frequency'] = 'daily'
        daily = Daily.new(**test_values)
        self.assertIn(daily.id, [d.id for d in Dailys()])
        self.assertEqual(daily.everyX, test_values['everyX'])
        self.assertEqual(daily.frequency, test_values['frequency'])
        daily.delete()

    def test_delete_daily(self):
        daily = Daily.new(text='Test deletion daily')
        daily.delete()
        self.assertNotIn(daily.id, [d.id for d in Dailys()])


class TestToDos(unittest.TestCase):
    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_read_todos(self):
        test_task_name = "Test todo"
        self.assertIn(test_task_name, [todo.text for todo in ToDos()])

    def test_add_todo(self):
        test_values = {}
        test_values['text'] = "Test creation todo"
        test_values['notes'] = "Test notes"
        test_values['date'] = "2016-12-25"
        test_values['priority'] = 2
        todo = ToDo.new(**test_values)
        self.assertIn(todo.id, [t.id for t in ToDos()])
        self.assertEqual(todo.text, test_values['text'])
        self.assertEqual(todo.notes, test_values['notes'])
        self.assertTrue(todo.date.startswith(test_values['date']))
        self.assertEqual(todo.priority, test_values['priority'])
        todo.delete()

    def test_delete_todo(self):
        todo = ToDo.new(text='Test deletion todo')
        todo.delete()
        self.assertNotIn(todo.id, [t.id for t in ToDos()])


class TestChecklists(unittest.TestCase):
    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_add_checklist_item(self):
        todo = ToDo.new(text='Test checklist todo')
        checklist_text = "Test checklist item"
        todo.add_to_checklist(checklist_text)
        checklist_titles = ([checklist_item['text']
                            for checklist_item in todo.checklist])
        self.assertIn(checklist_text, checklist_titles, "%s not in %s"
                      % (checklist_text, checklist_titles))
        todo.delete()

    def test_delete_checklist_item(self):
        todo = ToDo.new(text='Test checklist deletion todo')
        checklist_text = "I shouldn't be here"
        todo.add_to_checklist(checklist_text)
        checklist_id = ([checklist_item['id'] for checklist_item in
                        todo.checklist if
                        checklist_item['text'] == checklist_text][0])
        todo.delete_from_checklist(checklist_id)
        self.assertNotIn(checklist_text, [checklist_item['text'] for
                         checklist_item in todo.checklist])
        todo.delete()

    def test_edit_checklist_item(self):
        todo = ToDo.new(text='Test checklist edit todo')
        checklist_text = "You shouldn't see me."
        todo.add_to_checklist(checklist_text)
        edited_text = "I'm what you should see."
        checklist_item = {}
        checklist_item['id'] = [checklist_item['id'] for checklist_item in
                                todo.checklist if
                                checklist_item['text'] == checklist_text][0]
        checklist_item['text'] = edited_text
        todo.update_checklist_item(**checklist_item)
        edited_todo = ToDo(**API.Task.get(todo.id))
        checklist = ([checklist_item['text'] for checklist_item in
                     todo.checklist])
        self.assertNotIn(checklist_text, checklist)
        self.assertIn(edited_text, checklist)
        todo.delete()


class TestScoring(unittest.TestCase):
    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_score_task(self):
        daily = Daily.new(text='Test score daily')
        daily.score()
        self.assertTrue(daily.completed)
        daily.delete()

    def test_score_habit(self):
        habit = Habit.new(text='Test score habit', up=True, down=True)
        user = User()
        user.update_status()
        current_xp = user.profile['stats']['exp']
        current_hp = user.profile['stats']['hp']
        habit.score('up')
        user.update_status()
        self.assertNotEqual(current_xp, user.profile['stats']['exp'],
                            'XP has not changed')
        habit.score('down')
        user.update_status()
        self.assertNotEqual(current_hp, user.profile['stats']['hp'],
                            'HP has not changed')
        habit.delete()

    def test_score_todo(self):
        todo = ToDo.new(text='Test score todo')
        todo.score()
        self.assertTrue(todo.completed)
        todo.delete()

    def test_score_checklist(self):
        todo = ToDo.new(text='Test score checklist')
        checklist_text = "Check me off!"
        todo.add_to_checklist(checklist_text)
        todo.score_checklist_item(todo.checklist[0]['id'])
        self.assertTrue(todo.checklist[0]['completed'])
        todo.delete()


class TestTagging(unittest.TestCase):

    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_read_tags(self):
        self.assertTrue(len(Tags()) > 0)

    def test_add_tag(self):
        new_tag = Tag.new('New tag')
        self.assertIn(new_tag.id, [t.id for t in Tags()])
        new_tag.delete()

    def test_delete_tag(self):
        test_tag = Tag.new('Delete me')
        test_tag.delete()
        self.assertNotIn(test_tag.id, [t.id for t in Tags()])

    def test_rename_tag(self):
        test_tag = Tag.new('Edit me')
        test_tag.rename('Edited')
        self.assertEqual(test_tag.name, 'Edited')
        test_tag.delete()

    def test_apply_tag(self):
        test_tag = Tag.new('Apply me')
        test_daily = Daily.new(text='Tag me')
        test_daily.add_tag(test_tag)
        self.assertIn(test_tag.id, test_daily.tags)
        test_tag.delete()
        test_daily.delete()

    def test_remove_tag(self):
        test_tag = Tag.new('Remove me')
        test_daily = Daily.new(text='Untag me')
        test_daily.add_tag(test_tag)
        test_daily.remove_tag(test_tag)
        self.assertNotIn(test_tag.id, test_daily.tags)
        test_tag.delete()
        test_daily.delete()


class TestPurchasing(unittest.TestCase):

    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)
        User.update_status()

    def test_buy_healing_potion(self):
        healing_potion_cost = 25
        testing_habit = Habit.new(text='Test habit for stat manipulation',
                                  up=True, down=True)
        while User.gp < healing_potion_cost:
            testing_habit.score('up')
        if User.hp == User.maxHealth:
            testing_habit.score('down')
        testing_habit.delete()
        health_before_potion = User.hp
        Inventory.buy_health_potion()
        self.assertTrue(User.hp > health_before_potion,
                        "Before health: %s, Current health: %s" %
                        (health_before_potion, User.hp))

    def test_purchasables(self):
        purchasables = Inventory.Purchasables()
        self.assertTrue(len(purchasables) > 0, 'Purchasables 0 len')

    def test_buy_gear(self):
        purchasables = Inventory.Purchasables()
        buy_list_by_price = {item.value: item for item in purchasables}
        buy_cost = min(buy_list_by_price.keys())
        item_to_buy = buy_list_by_price[buy_cost]
        testing_habit = Habit.new(text='Test habit for stat manipulation',
                                  up=True, down=True)
        while User.gp < buy_cost:
            testing_habit.score()
        testing_habit.delete()
        item_to_buy.buy()
        self.assertIn(item_to_buy.key, [item.key for item in Inventory.Gear()])


class TestInventory(unittest.TestCase):

    def setUp(self):
        auth = API.Authentication
        auth.login(username, password)

    def test_list_purchasables(self):
        self.assertTrue(len(Inventory.Purchasables()) > 0)

    def test_list_equipped(self):
        self.assertTrue(len(Inventory.Equipped()) > 0)

    def test_list_gear(self):
        self.assertTrue(len(Inventory.Gear()) > 0)
