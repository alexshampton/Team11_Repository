package test;

import java.io.File;
import java.util.ArrayList;
import java.util.Collections;

public class renameImages {
    public static void main(String[] args) {
        ArrayList<String> oldName = new ArrayList<>();
        ArrayList<String> newName = new ArrayList<>();
        for (int i = 1; i <= 416; i++) {
            oldName.add("dst" + i + ".jpeg");
            newName.add("dstrain" + i + ".jpeg");
        }
        Collections.shuffle(newName);
        for (int i = 0; i < oldName.size(); i++) {
            File before = new File(oldName.get(i));
            File after = new File(newName.get(i));
            before.renameTo(after);
        }
    }
}