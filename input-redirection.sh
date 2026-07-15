cat > show-info.sh << 'EOF'
cat -e << END
USER=$USER
HOME=$HOME
SHELL=$SHELL
END
EOF

chmod +x show-info.sh