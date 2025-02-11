[![CI](https://github.com/mivek/ansible-role-pgbackrest/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mivek/ansible-role-pgbackrest/actions/workflows/ci.yml)

Ansible Role: PgBackrest
=========

Installs and configures PgBackrest on Debian/Ubuntu servers.

Requirements
------------

None.

Role Variables
--------------

    pgbackrest_version: 2.43
The version of pgbackrest to install.


    pgbackrest_user: postgres
The user running pgbackrest.


    pgbackrest_group: postgres
The group of the user running pgbackrest.

    pgbackrest_user_home: /var/lib/postgresql
Home directory of the user running pgbackrest

    pgbackrest_install_method: repository
Installation method of `pgbackrest`. Either repository or `source`.

    pgbackrest_configuration_global_options: []
List of global options to set. The structure is a list of objects with keys: `option` and `value`.

    pgbackrest_configuration_archive_push_options: []
List of archive push options to set. The structure is a list of objects with keys: `option` and `value`.

    pgbackrest_configuration_archive_get_options: []
List of archive get options to set. The structure is a list of objects with keys: `option` and `value`.

    pgbackrest_configuration_stanzas: []
List of stanzas. Each stanza has a name and a list of hosts. Each host has a list of options.

    pgbackrest_configuration_repositories: []
List of repositories configuration. Each repository is a list of `options`. Option are composed of a `name` and a `value`.

    pgbackrest_create_stanza: true
Whether to run the command to create the stanza.

    pgbackrest_check_stanza: true
Whether to run the command to verify the stanza configuration.

    pgbackrest_backup_cron: []
List of cron jobs to create to perform backups. All parameters from the `cron` modules are available.
Additionally, the `stanza` and `type` of backup are required. It is also possible to pass options as string in the parameter `options`.

    pgbackrest_user_private_key:
The private ssh key of the pgbackrest user.

    pgbackrest_user_authorized_keys: []
List of public ssh keys to add to the authorized keys of the user.

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        pgbackrest_user: postgres
        pgbackrest_group: postgres
        pgbackrest_configuration_global_options: []
        pgbackrest_configuration_stanzas:
        - name: demo
          hosts:
            - options:
                - name: path
                  value: '/var/lib/postgresql/{{ postgresql_version }}/main'
        pgbackrest_configuration_repositories:
          - options:
                - name: path
                  value: /var/lib/pgbackrest
                - name: retention-full
                  value: 2
                - name: cipher-pass
                  value: zWaf6XtpjIVZC5444yXB+cgFDFl7MxGlgkZSaoPvTGirhPygu4jOKOXf9LO4vjfO
                - name: cipher-type
                  value: aes-256-cbc
          - options:
              - name: path
                value: /var/lib/pgbackrest2
        pgbackrest_configuration_archive_push_options:
            - name: compress-level
              value: 3
        pgbackrest_backup_cron:
            - stanza: demo
              type: full
              weekday: SUN
              hour: 0
              minute: 0
              name: Full backup
            - stanza: demo
              type: diff
              day: '*'
              hour: 12
              minute: 0
              options: --backup-standby=y
              name: Incremental backup from standby
    roles:
        - mivek.pgbackrest

License
-------

BSD
