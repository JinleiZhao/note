#!/home/yaya/.pyenv/plugins/python 

from collections import namedtuple #命名元组

Disk = namedtuple('disk_', ['major_number','minor_number','device_name',
                          'read_count','read_merged_count','read_sections',
                          'time_spent_reading','write_count','write_merged_count',
                          'write_sections','time_spent_write','io_requests',
                          'time_spent_doing_io','weighte_time_spent_doing_io']) #相当于创建一个disk_对象，包含14个键(中括号中的为键名)

def get_disk_info(device):
    with open('/proc/diskstats') as f:
        for line in f:
            if line.split()[2] == device:
                #return Disk._make(line.split())  #Disk._replace(xx=xx) 对指定的键赋值
                return Disk(*(line.split()))#调用Disk，长度对应依次对各个键赋值，相当于Disk._make(line.split())
    raise RuntimeError('device ({0}) not found!'.format(device))

def main():
    disk_info = get_disk_info('sda')
    
    print(disk_info)
   
    print('磁盘写次数:{0}'.format(disk_info.write_count))
    print('磁盘写字节数:{0}'.format(int(disk_info.write_sections) * 512))
    print('磁盘写延时:{0}'.format(disk_info.time_spent_write))

if __name__ == '__main__':
    main()
