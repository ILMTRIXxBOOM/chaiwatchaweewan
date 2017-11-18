input_file = open("/Users/chaiwatchaweewan/Desktop/testcase.java", "r")

check_p_1 = False
check_p_2 = False


def line_num_count():
    num_lines = sum(1 for line in input_file)
    return num_lines


def fine_num_line():
    content = input_file.readlines()
    index = [x for x in range(len(content)) if 'public static' in content[x].lower()]
    return index


def line_number():
    line_num = map(str, fine_num_line())
    line_num = ''.join(line_num)
    line_num = int(line_num)
    return line_num


'''
def loop_indent():
    for line in input_file:
        if "for" in line:
            indent = line.fine("for")
            detected = line[:indent]
            return detected
            # if detected >= 2:
                # return True
        # return False 
'''

for_indent = 0
repetition_list = ["for(", "for (", "while(", "while ("]
selection_list = ["else if(", "else if (", "else {", "else{", "if(", "if ("]
declaration_list = ["Int ".lower(), "Double ".lower(), "String ".lower()]
reserve_list = ["public static boolean", "public static int", "public static string", "private static boolean",
                "private static int", "private static string"]
list_loop = []
list_if = []
list_indent = []
list_type = []
list_all = []
list_result = []

for line in input_file:
    p = 0
    if "public class" in line:

        check_p_1 = True
        next_line = next(input_file)

        if "public static" in next_line:

            for line_number in input_file:
                p = 0
                s = 0

                for reserve_word in reserve_list:
                    if reserve_word in line_number:
                        s = 1
                        break

                for r_type in repetition_list:
                    if r_type in line_number:
                        find_indent = line_number.find(r_type)
                        # list_indent.append(find_indent)
                        # list_type.append("R")
                        list_all.append("R-" + str(find_indent))
                        p = 1
                        break

                for s_type in selection_list:
                    if s_type in line_number:
                        find_indent = line_number.find(s_type)
                        # list_indent.append(find_indent)
                        # list_type.append("S")
                        list_all.append("S-" + str(find_indent))
                        break

                for d_type in declaration_list:
                    if d_type in line_number:
                        find_indent = line_number.find(d_type)
                        if p == 0 and s == 0:
                            # list_indent.append(find_indent)
                            # list_type.append("D")
                            list_all.append("D-" + str(find_indent))

                        if r_type and d_type in line_number:
                            break

            d = []
            s = ""
            i = 0
            '''
            for i, item in enumerate(list_all):
                # print item, str(i)
                if "R" in item[i]:
                    for next_item in list_all[i + 1]:
                        d.append(next_item)
                        s += next_item
                    if "D" in s:
                        print int(item[2]), int(s[2])
                        if int(item[2]) <= int(s[2]):
                            print 'good'

                    # print s
                    # break
                break
            '''

            for i in range(len(list_all)):

                if i < len(list_all) - 1:

                    # Repetition scanning module
                    if "R" in list_all[i]:

                        # print list_all[i][0], int(list_all[i][2:])

                        if "D" in list_all[i+1]:
                            # print list_all[i+1][0], int(list_all[i+1][2])
                            if int(list_all[i][2]) < int(list_all[i+1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "S" in list_all[i+1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) < int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "R" in list_all[i+1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) < int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")

                    # Declaration scanning module
                    if "D" in list_all[i]:

                        # print list_all[i][0], int(list_all[i][2:])

                        if "D" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "S" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "R" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")

                    # RSelection scanning module
                    if "S" in list_all[i]:

                        # print list_all[i][0], int(list_all[i][2:])

                        if "D" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "S" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")
                        elif "R" in list_all[i + 1]:
                            # print list_all[i + 1][0], int(list_all[i + 1][2])
                            if int(list_all[i][2]) <= int(list_all[i + 1][2:]):
                                list_result.append("P")
                            else:
                                list_result.append("X")

                        # print i
                        # print 'this', list_all[i]
                        # print 'next', list_all[i + 1]
            print list_result
            print list_all
            # print "Sequence of Statement:\t\t", list_type
            # print "Indentation:\t\t\t\t", list_indent
            '''
            for i in range(len(list_a)):

                if list_a[i] <= list_a[i + 1] + 2:
                    print 'Good indent'
                else:
                    print "not good"
                if i == 0:
                    break
            '''
