import ezdxf
from pathlib import Path


# =================================
# SHAFT CAD GENERATOR
# =================================

def create_shaft_dxf(
    diameter,
    length=200,
    output_file="shaft_design.dxf"
):

    # =================================
    # CREATE DXF DOCUMENT
    # =================================

    doc = ezdxf.new("R2010")

    msp = doc.modelspace()

    radius = diameter / 2


    # =================================
    # SHAFT OUTLINE
    # =================================

    # Top edge
    msp.add_line(
        (0, radius),
        (length, radius)
    )

    # Bottom edge
    msp.add_line(
        (0, -radius),
        (length, -radius)
    )

    # Left end
    msp.add_line(
        (0, -radius),
        (0, radius)
    )

    # Right end
    msp.add_line(
        (length, -radius),
        (length, radius)
    )


    # =================================
    # CENTER LINE
    # =================================

    msp.add_line(
        (0, 0),
        (length, 0)
    )


    # =================================
    # LENGTH DIMENSION
    # =================================

    dimension_y = -radius - 25
    arrow_size = 4

    # Extension lines
    msp.add_line(
        (0, -radius),
        (0, dimension_y)
    )

    msp.add_line(
        (length, -radius),
        (length, dimension_y)
    )

    # Dimension line
    msp.add_line(
        (0, dimension_y),
        (length, dimension_y)
    )

    # Left arrow
    msp.add_line(
        (0, dimension_y),
        (
            arrow_size,
            dimension_y + arrow_size / 2
        )
    )

    msp.add_line(
        (0, dimension_y),
        (
            arrow_size,
            dimension_y - arrow_size / 2
        )
    )

    # Right arrow
    msp.add_line(
        (length, dimension_y),
        (
            length - arrow_size,
            dimension_y + arrow_size / 2
        )
    )

    msp.add_line(
        (length, dimension_y),
        (
            length - arrow_size,
            dimension_y - arrow_size / 2
        )
    )

    # Length text
    msp.add_text(
        f"{length:.0f} mm",
        dxfattribs={
            "height": 5
        }
    ).set_placement(
        (
            length / 2 - 15,
            dimension_y + 4
        )
    )


    # =================================
    # DIAMETER DIMENSION
    # =================================

    dimension_x = length + 25

    # Extension lines
    msp.add_line(
        (length, radius),
        (dimension_x, radius)
    )

    msp.add_line(
        (length, -radius),
        (dimension_x, -radius)
    )

    # Dimension line
    msp.add_line(
        (dimension_x, -radius),
        (dimension_x, radius)
    )

    # Top arrow
    msp.add_line(
        (dimension_x, radius),
        (
            dimension_x - arrow_size / 2,
            radius - arrow_size
        )
    )

    msp.add_line(
        (dimension_x, radius),
        (
            dimension_x + arrow_size / 2,
            radius - arrow_size
        )
    )

    # Bottom arrow
    msp.add_line(
        (dimension_x, -radius),
        (
            dimension_x - arrow_size / 2,
            -radius + arrow_size
        )
    )

    msp.add_line(
        (dimension_x, -radius),
        (
            dimension_x + arrow_size / 2,
            -radius + arrow_size
        )
    )

    # Diameter text
    msp.add_text(
        f"DIA {diameter:.0f} mm",
        dxfattribs={
            "height": 5
        }
    ).set_placement(
        (
            dimension_x + 5,
            -3
        )
    )


    # =================================
    # TITLE
    # =================================

    msp.add_text(
        "AI GENERATED SHAFT",
        dxfattribs={
            "height": 7
        }
    ).set_placement(
        (
            0,
            radius + 20
        )
    )


    # =================================
    # SAVE FILE
    # =================================

    output_path = Path(output_file).resolve()

    doc.saveas(output_path)


    # =================================
    # CONFIRMATION
    # =================================

    print("================================")
    print("     CAD DRAWING GENERATED")
    print("================================")
    print(f"Diameter: {diameter:.2f} mm")
    print(f"Length: {length:.2f} mm")
    print(f"File: {output_path}")
    print("================================")

    return output_path


# =================================
# STANDALONE TEST
# =================================

if __name__ == "__main__":

    create_shaft_dxf(
        diameter=36,
        length=200,
        output_file="shaft_design.dxf"
    )