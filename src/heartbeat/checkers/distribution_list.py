from pkg_resources import WorkingSet


def distribution_list(request):
    return [
        {'name': distribution.project_name, 'version': distribution.version}
        for distribution in WorkingSet()
    ]
