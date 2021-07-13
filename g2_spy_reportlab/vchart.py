from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib import colors
from reportlab.graphics import renderPDF


class VChart(object):

    def __init__(self, x=None, y=None, hours=2, width=0, height=0) -> None:
        self.Xpadding = 10
        self.Ypadding = 10
        self.x = self.Xpadding
        self.y = self.Ypadding
        # self.Xticks_per_hour = 12
        self.Ytick_step = 10
        self.YMax = 250
        self.YMin = 0
        self.XMax = (hours * 60)
        self.XMin = 0
        self.Xtick_step = 5
        self.XScale = 2
        self.width = self.XMax * self.XScale + self.Xpadding * 2
        self.height = self.YMax + self.Ypadding * 2
        self.drawing = Drawing(width=self.width, height=self.height)

    def transformx(self, orig_x):
        return self.x + orig_x * self.XScale

    def transformy(self, orig_y):
        return self.y + orig_y

    def draw(self):
        self.add_v_grid_lines()
        self.add_h_grid_lines()

    def add_v_grid_lines(self):
        for x in range(self.XMin, self.XMax + self.Xtick_step, self.Xtick_step):
            grid_line = Line(self.transformx(x), self.transformy(self.YMin),
                             self.transformx(x), self.transformy(self.YMax))
            self.drawing.add(grid_line)

    def add_h_grid_lines(self):
        for y in range(self.YMin, self.YMax + self.Ytick_step, self.Ytick_step):
            grid_line = Line(self.transformx(self.XMin), self.transformy(y),
                             self.transformx(self.XMax), self.transformy(y),
                             strokeColor=colors.gray, strokeWidth=0.2)
            self.drawing.add(grid_line)


if __name__ == '__main__':
    v_chart = VChart()
    v_chart.draw()
    renderPDF.drawToFile(v_chart.drawing, 'vchart_main.pdf')
