xgettext -d en -o ../locale/en_US/LC_MESSAGES/en.pot ../data/download.py ../data/other.py ../data/products.py --from-code=utf-8
msgmerge ../locale/en_US/LC_MESSAGES/en.po ../locale/en_US/LC_MESSAGES/en.pot --update
pause