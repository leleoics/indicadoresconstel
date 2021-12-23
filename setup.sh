mkdir ./streamlit/

echo "\
[general]\n\
email = \"leonardocartografica@gmail.com\"\n\
" ./streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" ./streamlit/config.toml

echo "\
[theme]\n\
base =light\n\
primaryColor =#F63366\n\
backgroundColor =#FFFFFF\n\
secondaryBackgroundColor =#F0F2F6\n\
textColor =#262730\n\
font =sans serif\n\
" ./streamlit/config.toml