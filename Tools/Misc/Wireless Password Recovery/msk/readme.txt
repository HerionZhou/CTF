This folder contains Passcape Mask Files (*.msk)
with different mask sets. Should be used from within
the Passcape programs in mask attacks.

Short description of each mask is shown below.


========================================
File name		> 0-9.msk
Mask syntax		> test%d
Password range		> test0...test9
Total combinations 	> 10


File name		> 000000-zzzzzz.msk
Mask syntax		> %r(48-57,97-122)%l(1)%l(1)%l(1)%l(1)%l(1)
Password range		> 000000...zzzzzz
Total combinations 	> 2 176 782 336


File name		> 1980-2010.msk
Mask syntax		> test%d(1980-2010)
Password range		> test1980...test2010
Total combinations 	> 31


File name		> a-z,0-9.msk
Mask syntax		> test%r(48-57,97-122)
Password range		> test0...testz
Total combinations 	> 36


File name		> date.msk
Mask syntax		> %d(1-12)%r(45-47)%d(1-31)%l(2)%d(1980-2010)
Password range		> 1-1-1980...12/31/2010
Total combinations 	> 103 788


File name		> links.msk
Mask syntax		> %c%r(33-63)%c%l(2)%c%l(2)%c
Password range		> a!a!a!a...z?z?z?z
Total combinations 	> 13 613 772 016


File name		> symbol14.msk
Mask syntax		> test%r(33-33,35-38,40-43,45-45,61-61,64-64,94-95)
Password range		> test!...test_
Total combinations 	> 14


File name		> symbols.msk
Mask syntax		> %#test%#
Password range		> test...~test~
Total combinations 	> 1 089


File name		> russian.msk
Mask syntax		> %r(160-175,241-241,224-239)%l(1)%l(1)%l(1)%l(1)%l(1)
Password range		>       ...ïïïïïï
Total combinations 	> 1 291 467 969
========================================
