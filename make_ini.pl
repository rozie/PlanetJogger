#!/usr/bin/perl

# script to generate feed part of planet configuration with alphabetical order
# INPUT exactly 4 arguments, space separated. 3rd is feed URL, 4th is name

use strict;
use warnings;

my %feeds=();

while (<>){
	if (! /^#/){
		chomp;
		if (/(\S+)\s+(\S+)\s+(http\S+)\s+(\S+)/){
			$feeds{$4}=$3;
		}
		else {
			print "ERROR Wrong format in line: $_\n"
		}
	}
}

foreach my $name (sort keys %feeds){
	print "[$feeds{$name}]\n";
	print "name = $name\n\n"
}
