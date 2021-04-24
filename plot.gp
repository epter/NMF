#플랏

set datafile separator ","
set size square
set palette defined ( -1 '#ffffff', 0 '#000090',1 '#000fff',2 '#0090ff',3 '#0fffee',4 '#90ff70',5 '#ffee00',6 '#ff7000',7 '#ee0000',8 '#7f0000')
set cbrange [0:100]
set xrange [0:24]
set yrange [0:100]
plot "input.csv" matrix with image #csv 파일 이름 
