mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"leonardocartografica@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

echo "\
[theme]\n\
base = \"light\"\n\
" > ~/.streamlit/credentials.toml