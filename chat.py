
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = [] #設清單來儲存
	person = None #person還沒有設定出來
	for line in lines:
		if line == 'Allen':
			person = 'Allen' #設變數來存暫時的東西
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值的話
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines) #有覆蓋lines的感覺
	write_file('result.txt', lines)

main()