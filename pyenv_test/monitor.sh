#!/bin/bash

cpu_idle=$(top -n2 | grep 'Cpu' | tail -n 1 | awk '{print $8}')

echo "$cpu_idle"
cpu_usage=$(echo "100 - $cpu_idle" | bc)

mem_free=$(free -m | awk 'NR==2{print $4 + $6 + $7}') 
mem_total=$(free -m | awk 'NR==2{print $2}')
#free -m 查看内存使用，awk NR==2 只查看第二行  $n 第n列

echo $mem_free 
mem_used=$(echo "$mem_total - $mem_free" | bc )
mem_rate=$(echo "$mem_used * 100 / $mem_total" | bc)

disk_usage=$(df -h / | tail -n 1 | awk '{print $5}' )
disk_used=$(df -h / | tail -n 1 | awk '{print $3}')

echo "cpu利用率:$cpu_usage %"
echo "内存使用量:$mem_used M"
echo "内存利用率:$mem_rate %"
echo "磁盘空间使用量:$disk_used"
echo "磁盘空间使用率:$disk_usage"

cat << EOF
<html>
<head><title >监控信息</ title>
<body>
<table>
<tr><td>cpu利用率</td><td>$cpu_usage</td></tr>
<tr><td>内存使用量</td><td>$mem_used</td></tr>
<tr><td>内存利用率</td><td>$mem_rate</td></tr>
<tr><td>磁盘空间使用量</td><td>$disk_used</td></tr>
<tr><td>磁盘空间利用率</td><td>$disk_usage</td></tr>
</table>
</body>
</html>
EOF 
