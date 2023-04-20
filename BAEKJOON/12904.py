S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)




# 자바 풀이, 이걸로 해야 시간 초과 안남
# import java.util.Scanner;

# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);

#         String S = scanner.nextLine();
#         String T = scanner.nextLine();
#         scanner.close();

#         while (S.length() < T.length()) {
#             if (T.charAt(T.length() - 1) == 'A') {
#                 T = T.substring(0, T.length() - 1);
#             } else if (T.charAt(T.length() - 1) == 'B') {
#                 T = new StringBuilder(T.substring(0, T.length() - 1)).reverse().toString();
#             }
#         }

#         if (S.equals(T)) {
#             System.out.println(1);
#         } else {
#             System.out.println(0);
#         }
#     }
# }


