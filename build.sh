#!/usr/bin/env bash
cd client-vue
npm run build
cd ..
cp client-vue/dist/index.html server/frontend/templates/frontend/index.html
cp -r client-vue/dist/static/ server/frontend/
