from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="Name")
    app.group.modify_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
    #old_groups = app.group.get_group_list()
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #app.group.modify_first_group(Group(header="Logo"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
