#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return "Hello " + msg + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(type='str')
        )
    )

    message = module.params['msg']
    output = sayHello( message )

    # Success with no change
    module.exit_json( result=output, changed=False )

    # Success with change
    #module.exit_json( result=output, changed=True )

    # Report failure
    #module.fail_json( msg="Unknown error occurred." )


if __name__ == '__main__':
    main()
