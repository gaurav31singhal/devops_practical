from ansible.module_utils.basic import *


def main():
  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  username = module.params.get("username")

  [entry.pw_shell for entry in pwd.getpwall() if entry.pw_name=="root"][0]

main()
