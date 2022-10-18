import matplotlib.pyplot as plt
import numpy as np

def parse_txt(filename):
    with open(filename, newline='') as file:
        data_lm = []
        data_lb = []
        data_rm = []
        data_rb = []
        for line in file:
            line= line.replace('[', '')
            line= line.replace(']', '')
            l = line.split(',')
            print(l)
            # l = np.array(line)
            # print(line)
            data_lm.append(float(l[0]))
            data_lb.append(float(l[1]))
            data_rm.append(float(l[2]))
            data_rb.append(float(l[3]))
    return data_lm, data_lb, data_rm, data_rb

def parse_csv(filename):
    with open(filename, newline='') as file:
        data_lm = []
        data_lb = []
        data_rm = []
        data_rb = []
        count = 0
        for line in file:
            if count > 3:
                l = line.split(' ')
                print(l)
                data_lm.append(float(l[0]))
                data_lb.append(float(l[1]))
                data_rm.append(float(l[2]))
                data_rb.append(float(l[3]))
            count += 1
    return data_lm, data_lb, data_rm, data_rb

# neutral = parse_txt('neutral.txt')
# left = parse_txt('left_arm_up.txt')
# right = parse_txt('right_arm_up.txt')

neutral = parse_csv('initial_data/neutral2.csv')
left = parse_csv('initial_data/left_down.csv')
right = parse_csv('initial_data/right_down.csv')



# plot single stream
# plt.figure()
# plt.plot(neutral[0])
# plt.plot(neutral[1])
# plt.plot(neutral[2])
# plt.plot(neutral[3])
# plt.legend()
# plt.show()


# plot three streams by feature
plt.figure()
plt.plot(neutral[0][25:], label='n')
plt.plot(left[0][25:], label='l')
plt.plot(right[0][25:], label='r')
plt.legend()
plt.show()

plt.figure()
plt.plot(neutral[1][25:], label='n')
plt.plot(left[1][25:], label='l')
plt.plot(right[1][25:], label='r')
plt.legend()
plt.show()

plt.figure()
plt.plot(neutral[2][25:], label='n')
plt.plot(left[2][25:], label='l')
plt.plot(right[2][25:], label='r')
plt.show()

plt.figure()
plt.plot(neutral[3][25:], label='n')
plt.plot(left[3][25:], label='l')
plt.plot(right[3][25:], label='r')
plt.show()