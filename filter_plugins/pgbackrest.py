

def repositories_path(repositories_list):
    """
    Returns a list of paths for local repositories (type is posix, cifs,
    or not set since posix is the default).
    """
    local_types = {'posix', 'cifs'}
    return [repository['options']['path'] for repository in repositories_list
            if 'path' in repository['options']
            and repository['options'].get('type', 'posix') in local_types]


def spool_path(options_map):
    """
    Returns the spool path from the options map.
    """
    return [options_map['spool-path']] if 'spool-path' in options_map else []


class FilterModule(object):

    def filters(self):
        return {
            'repositories_path': repositories_path,
            'spool_path': spool_path
        }
