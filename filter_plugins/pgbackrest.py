

def repositories_path(repositories_list):
    """
    Returns a list of paths in the options of repositories.
    """
    return [option['value'] for repository in repositories_list for option
            in repository['options'] if option['name'] == 'path']


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
