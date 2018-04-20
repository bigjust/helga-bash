from helga.plugins import command

@command('bash', help='like hulk-smash, but with ')
def bash(client, channel, nick, message, cmd, args):
    return 'Success!'
