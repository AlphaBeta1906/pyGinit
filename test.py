from pyGinit import repo


def test_add_license():
    for v in repo.license_dict:
        print(v)
        assert repo.addLicense(v, test=True) == 200


def test_add_gitignore():
    assert repo.add_gitignore("Python", test=True,addtional_gitignore=None) == 200


