#!/usr/bin/env bash
cd client-vue
npm run build
cd ..
cp client-vue/dist/index.html server/frontend/templates/frontend/index.html
rm -rf server/frontend/static/
cp -r client-vue/dist/static/ server/frontend/
