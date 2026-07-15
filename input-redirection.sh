cat > show-info.sh << 'EOF'

cat -e << INFO
The current directory is: $PWD
The default paths are: $PATH
The current user is: azraji
INFO

EOF

chmod +x show-info.sh