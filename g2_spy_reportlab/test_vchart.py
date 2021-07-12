import pytest
from reportlab.graphics import renderPDF

from vchart import VChart


@pytest.fixture
def v_chart():
    chart = VChart()
    return chart


def test_axises(v_chart):
    assert v_chart.width == 260
    assert v_chart.height == 270


def get_bounds(args):
    return (args[1].x1, args[1].x2, args[1].y1, args[1].y2)


def test_mock_object(v_chart, mocker):
    from vchart import Drawing, Line
    spy = mocker.spy(Line, "__init__")
    mock_drawing_add = mocker.patch.object(Drawing, "add", autospec=True)
    v_chart.draw()
    renderPDF.drawToFile(v_chart.drawing, 'vchart_demo.pdf')
    assert spy.call_count == 51
    assert mock_drawing_add.call_count == 51
    assert get_bounds(mock_drawing_add.call_args_list[-1][0]) == (10, 250,260,260)


def test_mock_spy(v_chart, mocker):
    from vchart import Drawing, Line
    spy = mocker.spy(Line, "__init__")
    mock_drawing_add = mocker.spy(Drawing, "add")
    v_chart.draw()
    renderPDF.drawToFile(v_chart.drawing, 'vchart_demo.pdf')
    assert spy.call_count == 51
    assert mock_drawing_add.call_count == 51
    assert get_bounds(mock_drawing_add.call_args_list[-1][0]) == (10, 250,260,260)

