from context_manager import FileHandler
from unittest import TestCase


class TestContextManager(TestCase):
    def setUp(self):
        self.file_handler = FileHandler("cars.csv")
        self.first_3_lines = [
            "Make,Model,Type,Origin,DriveTrain,MSRP,Invoice,EngineSize,Cylinders,Horsepower,MPG_City,MPG_Highway,Weight,Wheelbase,Length\n",
            "Acura,MDX,SUV,Asia,All,36945.0,33337.0,3.5,6.0,265.0,17.0,23.0,4451.0,106.0,189.0\n",
            "Acura,RSX Type S 2dr,Sedan,Asia,Front,23820.0,21761.0,2.0,4.0,200.0,24.0,31.0,2778.0,101.0,172.0\n",
        ]
        self.next_3_lines = [
            "Acura,TSX 4dr,Sedan,Asia,Front,26990.0,24647.0,2.4,4.0,200.0,22.0,29.0,3230.0,105.0,183.0\n",
            "Acura,TL 4dr,Sedan,Asia,Front,33195.0,30299.0,3.2,6.0,270.0,20.0,28.0,3575.0,108.0,186.0\n",
            "Acura,3.5 RL 4dr,Sedan,Asia,Front,43755.0,39014.0,3.5,6.0,225.0,18.0,24.0,3880.0,115.0,197.0\n",
        ]

    def test_read_lines_generator(self):
        """Test if FileHandler.read_lines() return one line from file when
        lines_left is set to 1 and this method is called multiple times.
        """
        with self.file_handler as file:
            self.assertEqual(file.read_lines(1), [self.first_3_lines[0]])
            self.assertEqual(file.read_lines(1), [self.first_3_lines[1]])
            self.assertEqual(file.read_lines(1), [self.first_3_lines[2]])

    def test_read_lines_lines_left(self):
        """Test if FileHandler.read_lines() with lines_left higher than 1 return
        correct number of lines.
        """
        with self.file_handler as file:
            self.assertEqual(file.read_lines(lines_left=3), self.first_3_lines)

    def test_read_lines_call_fm_more(self):
        """Test if FileHandler.readlines() works correctly when same instance
        is called multiple times. Test if correct lines are displayed and
        self.last_index attribute is changing between calling same instances
        of FileHandler.
        """
        self.assertEqual(self.file_handler.last_index, 0)
        with self.file_handler as file:
            self.assertEqual(file.read_lines(lines_left=3), self.first_3_lines)
        self.assertEqual(self.file_handler.last_index, 3)
        with self.file_handler as file:
            self.assertEqual(file.read_lines(lines_left=3), self.next_3_lines)
        self.assertEqual(self.file_handler.last_index, 6)
