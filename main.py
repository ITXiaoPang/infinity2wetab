#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json


def load_infinty():
    ret = []
    with open('infinityBackup.infinity', 'r') as f_infinity:
        d_infinity = json.load(f_infinity)
        d_infinity_data = d_infinity.get('data', {})
        d_infinity_site = d_infinity_data.get('site', [])
        d_infinity_sites = d_infinity_site.get('sites', [])
        for _page in d_infinity_sites:
            for _folder in _page:
                ret.append(_folder)

    return ret


def dumps_wetab(infinty_folders: list):
    with open('wetab.data', 'r') as f_wetab:
        d_wetab = json.load(f_wetab)
        d_wetab_data = d_wetab.get('data', {})
        d_wetab_store_icon = d_wetab_data.get('store-icon', {})
        d_wetab_icons = d_wetab_store_icon.get('icons', [])
    for folder in infinty_folders:
        template_category = dict(
            id=folder.get('id', '').replace('folderId-', 'category-'),
            iconClass="icon-jianzhu",
            name=folder.get('name', ''),
            updateTime=folder.get('updateTime', ''),
            children=[]
        )
        template_category_children = []
        folder_children = folder.get('children', [])
        for _ in folder_children:
            template_site = dict(
                name=_.get('name', ''),
                target=_.get('target', ''),
                type='site',
                bgType='image',
                bgColor='rgba(0, 0, 0, 0)',
                bgImage=_.get('bgImage', ''),
                origin=_.get('uuid', ''),
                id=_.get('id', '').replace('site-', 'icon-'),
                updateTime=0
            )
            template_category_children.append(template_site)
        template_category['children'] = template_category_children
        d_wetab_icons.append(template_category)

    d_wetab['data']['store-icon']['icons'] = d_wetab_icons

    with open('new_wetab.data', 'w') as f_wetab_w:
        json.dump(d_wetab, f_wetab_w)


if __name__ == '__main__':
    _infinty_folders = load_infinty()
    dumps_wetab(_infinty_folders)
