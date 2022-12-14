#!/usr/bin/perl -w
# clientfork.pl - a client that forks to
# read from STDIN and write to a server
use strict;
use IO::Socket;
my $host = shift || 'localhost';
my $port = shift || 7890;
my $sock = new IO::Socket::INET(
                   PeerAddr => $host,
                   PeerPort => $port,
                   Proto    => 'tcp');
$sock or die "no socket :$!";
$sock->autoflush(1);
my($in, $buf, $kid);
die "fork fail: $!" unless defined($kid = fork);
if ($kid) {
    # parent reads from STDIN, prints to socket
    while (defined($in = <STDIN>)) {
   print $sock $in;
    }
    # kill the child process
    kill(TERM => $kid);
} else {
    # child reads from socket, prints to STDOUT
    while (defined($buf = <$sock>)) {
   print $buf;
    }
    close $sock;
}
 
