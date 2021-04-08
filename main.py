"""თქვენი ამოცანაა დაწეროთ პროგრამა, რომელიც მასწავლებლებს საშუალებას მისცემს
შექმნან ტესტი. შექმენით კლასი სახელწოდებით Testpaper. ობიექტის ინიციალიზაციისას
შესაძლებელი უნდა იყოს მინიმალური ქულის მითითებაც. ასევე უნდა იყოს მითითებული
საგანის სახელწოდება და სწორი პასუხების სია. კლასში გექნებათ შემდეგი ატრიბუტები:

● subject - საგნის დასახელება
● mark_scheme სწორი პასუხების ჩამონათვალი
● pass_mark გამსვლელი ქულა

ასევე შექმენით კლასი Student შემდეგი ფუნქციონალით:
● შეუქმენით ატრიბუტი tests_taken ნაგულისხმევი მნიშვნელობით 'No tests taken'
● შეუქმენით მეთოდი take_test, რომელიც მიიღებს Testpaper კლასის ობიექტს და
სტუდენტის პასუხების სიას. შეადარეთ სტუდენტის პასუხები ტესტის პასუხებს და
მიღებული შედეგი შეინახეთ სტუდენტის ატრიბუტში tests_taken ისე როგორც
მაგალითშია ნაჩვენები.
● მას შემდეგ, რაც სტუდენტი პირველ ტესტს დაწერს, tests_taken ატრიბური
გახდება dict ტიპის.
● ყველა გასაღები(key) tests_taken დიქშენარში იქნება Testpaper კლასის ობიექტის
subject ატრიბუტიდან აღებული, ხოლო მნიშვნელობა(value) იქნება მაგალითში
მოცემული სტრიქონის მსგავსი.(ჩააბარა თუ არა ტესტი და მიღებული შედეგის
მნიშვნელობა პროცენტებში.)
მაგალითი:
შენიშვნა:
● პროცენტები დაამრგვალეთ უახლოეს მთელ რიცხვამდე
● გახსოვდეთ, რომ test_taken ცვლადმა უნდა დააბრუნოს 'No tests taken' სტრიქონი, თუ
სტუდენტს არ აქვს ტესტი დაწერილი.

"""


class Testpaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, tests_taken="No tests taken"):
        self.tests_taken = tests_taken

    def take_test(self, test: Testpaper, answers):
        if len(answers) != len(test.mark_scheme):
            raise ValueError("Answers list is not the same length")
        correct = 0
        for i in range(len(test.mark_scheme)):
            if test.mark_scheme[i] == answers[i]:
                correct += 1
        percentage = round(correct/len(test.mark_scheme) * 100)
        pass_score = int(test.pass_mark.replace("%", ""))
        passed = True if percentage >= pass_score else False
        if isinstance(self.tests_taken, str):
            self.tests_taken = {}
        self.tests_taken[test.subject] = f"{'Passed!' if passed else 'Failed!'} ({percentage}%)"





if __name__ == '__main__':
    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "60%")

    student1 = Student()
    student2 = Student()

    print(student1.tests_taken)
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    print(student1.tests_taken)

    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    print(student2.tests_taken)
