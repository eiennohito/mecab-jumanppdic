#!/usr/bin/env perl
# 広範に      (こうはんに) 広範だ     形容詞         ナ形容詞       ダ列基本連用

# 富市 とみいち 富市 名詞 6 人名 5 * 0 * 0 NI
# 及ぼす およぼす 及ぼす 動詞 2 * 0 子音動詞サ行 5 基本形 2 "代表表記:及ぼす"

while (<>) {
    chomp;
    next if (/^@ /);
    if (/EOS/) {
	print "EOS\n";
    } else {
	my @t = split /\s+/, $_;
        print "$t[0]\t$t[3],$t[5],$t[7],$t[9],$t[2],$t[1]\n";
    }
}
