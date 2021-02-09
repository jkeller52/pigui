#deploy.py
server.shell(
    name='hdmi1',  # optional name for the operation
    commands='sudo ./documents/github/pigui/hdmi1.py',
)

# Define some state - this operation will do nothing on subsequent runs
#apt.packages(
#    name='Ensure the vim apt package is installed',
#    packages=['vim'],
#    sudo=True,  # use sudo when installing the packages
#)