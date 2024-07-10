import java.util.Scanner;

public class Playfair {
    private int length = 0;
    private String[][] table;

    public static void main(String args[]) {
        Playfair pf = new Playfair();
    }

    private Playfair() {
        System.out.print("Enter the Key: ");
        Scanner sc = new Scanner(System.in);
        String key = parseString(sc);
        while (key.equals(""))
            key = parseString(sc);
        table = generateTable(key);

        System.out.print("Enter the Message: ");
        String input = parseString(sc);
        while (input.equals(""))
            input = parseString(sc);

        String output = encrypt(input);

        printMatrix(table);

        System.out.println("Encrypted Message: " + output);
    }

    // Parse user input and preprocess it
    private String parseString(Scanner sc) {
        String parse = sc.nextLine();
        parse = parse.toUpperCase().replaceAll("[^A-Z]", "").replace("J", "I");
        return parse;
    }

    // Generate the Playfair cipher table based on the key
    private String[][] generateTable(String key) {
        String[][] playfairTable = new String[5][5];
        String keyString = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ";

        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                playfairTable[i][j] = "";

        for (int k = 0; k < keyString.length(); k++) {
            boolean repeat = false;
            boolean used = false;
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if (playfairTable[i][j].equals("" + keyString.charAt(k))) {
                        repeat = true;
                    } else if (playfairTable[i][j].equals("") && !repeat && !used) {
                        playfairTable[i][j] = "" + keyString.charAt(k);
                        used = true;
                    }
                }
            }
        }
        return playfairTable;
    }

    // Encrypt the input message using the Playfair cipher
    private String encrypt(String in) {
        length = (int) in.length() / 2 + in.length() % 2;

        for (int i = 0; i < (length - 1); i++) {
            if (in.charAt(2 * i) == in.charAt(2 * i + 1)) {
                in = new StringBuffer(in).insert(2 * i + 1, 'X').toString();
                length = (int) in.length() / 2 + in.length() % 2;
            }
        }

        String[] digraph = new String[length];

        for (int j = 0; j < length; j++) {
            if (j == (length - 1) && in.length() / 2 == (length - 1))
                in = in + "X";
            digraph[j] = in.charAt(2 * j) + "" + in.charAt(2 * j + 1);
        }

        StringBuilder out = new StringBuilder();
        String[] encDigraphs = encodeDigraph(digraph);

        for (String encDigraph : encDigraphs)
            out.append(encDigraph);

        return out.toString();
    }

    // Encode the digraphs based on Playfair cipher rules
    private String[] encodeDigraph(String[] di) {
        String[] encipher = new String[length];

        for (int i = 0; i < length; i++) {
            char a = di[i].charAt(0);
            char b = di[i].charAt(1);
            int[] pointA = getPoint(a);
            int[] pointB = getPoint(b);

            if (pointA[0] == pointB[0]) {
                pointA[1] = (pointA[1] + 1) % 5;
                pointB[1] = (pointB[1] + 1) % 5;
            } else if (pointA[1] == pointB[1]) {
                pointA[0] = (pointA[0] + 1) % 5;
                pointB[0] = (pointB[0] + 1) % 5;
            } else {
                int temp = pointA[1];
                pointA[1] = pointB[1];
                pointB[1] = temp;
            }

            encipher[i] = table[pointA[0]][pointA[1]] + "" + table[pointB[0]][pointB[1]];
        }

        return encipher;
    }

    // Get the coordinates of a character in the Playfair cipher table
    private int[] getPoint(char c) {
        int[] point = new int[2];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (c == table[i][j].charAt(0)) {
                    point[0] = i;
                    point[1] = j;
                    return point;
                }
            }
        }

        return point;
    }

    // Print the Playfair cipher table
    private void printMatrix(String[][] printTable) {
        System.out.println("Playfair Cipher Key Matrix: ");
        for (String[] row : printTable) {
            for (String element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
    }
}
