package datasetapp;

import com.github.sarxos.webcam.Webcam;
import com.github.sarxos.webcam.WebcamPanel;
import com.github.sarxos.webcam.WebcamResolution;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;

public class DatasetApp extends JFrame{
    private JPanel panel;
    private JButton snapshot;
    private JRadioButton []options;
    
    private JPanel northPanel;
  
    public DatasetApp(){
        super("Dataset Application");
        
        setSize(new Dimension(800, 600));
        
        panel = new JPanel();
        
        panel.setLayout(new BorderLayout());
        
        snapshot = new JButton("Snapshot");
        panel.add(snapshot, BorderLayout.SOUTH);
        
        northPanel = new JPanel();
        northPanel.setLayout(new GridLayout(1, 4));
        
        options = new JRadioButton[4];
        
        options[0] = new JRadioButton("Rock");
        options[0].setActionCommand("rocks");
        
        options[1] = new JRadioButton("Paper");
        options[1].setActionCommand("paper");
        
        options[2] = new JRadioButton("Scissors");
        options[2].setActionCommand("scissor");
        
        options[3] = new JRadioButton("New game round video");
        options[3].setActionCommand("videos");
        options[3].setEnabled(false);
        
        options[0].setSelected(true);
                
        ButtonGroup optionsGroup = new ButtonGroup();
        
        for (JRadioButton option : options)
        {
            optionsGroup.add(option);
        }
       
        for (JRadioButton option : options)
        {
            northPanel.add(option, BorderLayout.NORTH);
        }
        
        panel.add(northPanel, BorderLayout.NORTH);
        
        Webcam webcam = Webcam.getDefault();
        webcam.setViewSize(new Dimension(640, 480));
        webcam.open();       

        WebcamPanel webcamPanel = new WebcamPanel(webcam);
        webcamPanel.setMirrored(true);
        
        panel.add(webcamPanel, BorderLayout.CENTER);
        
        add(panel);
        
        snapshot.addActionListener((ActionEvent e) -> {
            try {
                BufferedImage image = webcam.getImage();
                
                int width = image.getWidth();
                int height = image.getHeight();

                for(int y = 0; y < height; y++){
                  for(int x = 0; x < width/2; x++){
                    int p1 = image.getRGB(x, y);
                    int p2 = image.getRGB(width-x-1, y);
                    
                    image.setRGB(x, y, p2);
                    image.setRGB(width-x-1, y, p1);
                  }
                }
                
                File dir = new File("dataset/" + optionsGroup.getSelection().getActionCommand());
                dir.mkdirs();
                int k = dir.listFiles().length+1;
                
                ImageIO.write(image, "PNG", new File("dataset/" + optionsGroup.getSelection().getActionCommand() + "/" + k + ".png"));
            } 
            catch (IOException ex) {
                Logger.getLogger(DatasetApp.class.getName()).log(Level.SEVERE, null, ex);
            }
        });
        
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args){
        JFrame jf = new DatasetApp();
        jf.setVisible(true);
    }
}
