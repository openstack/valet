
#sudo tox -epy27 -- '--concurrency=1' $*

# EXAMPLE:
# ./run_test '(TestAffinity)'

# run specific tests:
# sudo tox -epy27 --  '(TestAffinity|TestDiversity)'
# run all tests in a loop until failure

#sudo tox -- --until-failure
# run specific tests:
# sudo tox -epy27 --  '(TestAffinity|TestDiversity)'

# isolate
# sudo tox -- --isolated

# run all tests until failure
# sudo tox -- --until-failure
 
# unparallel running (serial)
# sudo tox -epy27 -- '--concurrency=1'

# use  commands = ostestr --slowest '{posargs}' in file tox.ini
# http://docs.openstack.org/developer/os-testr/ostestr.html#running-tests
