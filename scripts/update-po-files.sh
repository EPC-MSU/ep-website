# general + eyepoint
xgettext -d en -o ../sites/eyepoint/locale/en_US/LC_MESSAGES/en.pot \
  ../site_engine/specification/general.py \
  ../sites/eyepoint/data/download.py ../sites/eyepoint/data/other.py ../sites/eyepoint/data/products.py \
  --from-code=utf-8
msgmerge ../sites/eyepoint/locale/en_US/LC_MESSAGES/en.po ../sites/eyepoint/locale/en_US/LC_MESSAGES/en.pot --update

# general + usbadc10
xgettext -d en -o ../sites/usbadc10/locale/en_US/LC_MESSAGES/en.pot \
  ../site_engine/specification/general.py \
  ../sites/usbadc10/data/download.py ../sites/usbadc10/data/other.py ../sites/usbadc10/data/products.py \
  --from-code=utf-8
msgmerge ../sites/usbadc10/locale/en_US/LC_MESSAGES/en.po ../sites/usbadc10/locale/en_US/LC_MESSAGES/en.pot --update

# general + mdrive
xgettext -d en -o ../sites/mdrive/locale/en_US/LC_MESSAGES/en.pot \
  ../site_engine/specification/general.py \
  ../sites/mdrive/data/download.py ../sites/mdrive/data/other.py ../sites/mdrive/data/products.py \
  --from-code=utf-8
msgmerge ../sites/mdrive/locale/en_US/LC_MESSAGES/en.po ../sites/mdrive/locale/en_US/LC_MESSAGES/en.pot --update