read -p "Enter your name [Richard]: " name
name=${name:-Richard}
echo $name


myVar=$(openssl rand -hex 32)
echo $myVar

