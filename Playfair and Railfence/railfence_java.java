import java.util.Scanner;

public class RailFenceCipher {
    private int numRails;

    public RailFenceCipher(int numRails) {
        this.numRails = numRails;
    }

    // Method to decrypt the data using straight (vertical and horizontal) logic
    private String decryptData(String data) {
        char[] decrypted = new char[data.length()];
        int n = 0;
        for (int rail = 0; rail < numRails; rail++) {
            int index = rail;
            while (index < data.length()) {
                decrypted[index] = data.charAt(n++);
                index = index + numRails;
            }
        }
        return new String(decrypted);
    }

    // Method to encrypt the data using straight (vertical and horizontal) logic
    private String encryptData(String data) {
        char[] encrypted = new char[data.length()];
        int n = 0;

        for (int rail = 0; rail < numRails; rail++) {
            int index = rail;
            while (index < data.length()) {
                encrypted[n++] = data.charAt(index);
                index = index + numRails;
            }
        }
        return new String(encrypted);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the Number of Rails: ");
        int numRails = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character

        System.out.print("Enter the Message: ");
        String data = scanner.nextLine().toUpperCase();

        RailFenceCipher railFenceCipher = new RailFenceCipher(numRails);

        // Display original data
        System.out.println("Original Message: " + data);

        // Encrypt the data and display the encryption matrix
        String encrypted = railFenceCipher.encryptData(data);
        System.out.println("Encrypted Message: " + encrypted);
        System.out.println("Encryption Matrix:");

        // Display the encryption matrix
        for (int rail = 0; rail < numRails; rail++) {
            for (int i = 0; i < encrypted.length(); i++) {
                if (i % numRails == rail) {
                    System.out.print(encrypted.charAt(i) + "\t");
                } else {
                    System.out.print(".\t"); // Placeholder for empty cells
                }
            }
            System.out.println();
        }

        System.out.println();

        // Decrypt the data and display the decryption matrix
        String decrypted = railFenceCipher.decryptData(encrypted);
        System.out.println("Decrypted Message: " + decrypted);
        System.out.println("Decryption Matrix:");

        // Display the decryption matrix
        for (int rail = 0; rail < numRails; rail++) {
            for (int i = 0; i < decrypted.length(); i++) {
                if (i % numRails == rail) {
                    System.out.print(decrypted.charAt(i) + "\t");
                } else {
                    System.out.print(".\t"); // Placeholder for empty cells
                }
            }
            System.out.println();
        }

        scanner.close();
    }
}
