mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"leonardocartografica@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
base = "light"\n\
primaryColor = "white"\n\
backgroundColor = "white"\n\
secondaryBackgroundColor = "purple"\n\
textColor = "black"\n\
font = "sans serif"\n\
" > ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml