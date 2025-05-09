import sys
import pymupdf

A4Width = 595
A4Height = 842

def page_bounding_box(page):
    rects = []

    # Get text bounding boxes
    for block in page.get_text("blocks"):
        rect = pymupdf.Rect(block[:4])
        rects.append(rect)

    # Get image bounding boxes
    for img in page.get_images(full=True):
        bbox = page.get_image_bbox(img)
        rects.append(bbox)

    # Get drawings bounding boxes
    for item in page.get_drawings():
        rect = item["rect"]
        rects.append(rect)

    if not rects:
        return None

    # Merge bounding boxes
    bounding_box = rects[0]
    for rect in rects[1:]:
        bounding_box |= rect

    return bounding_box

def main(argv):
    input_filename = argv[1]
    output_filename = argv[2]
    doc = pymupdf.open(input_filename)

    rects = [page_bounding_box(page) for page in doc]

    bounding_box = rects[0]
    for rect in rects[1:]:
        bounding_box |= rect

    print(bounding_box)

    for page in doc:
        #shape = page.new_shape()
        #shape.draw_rect(bounding_box)
        #shape.finish(color=(1,0,0))
        #shape.draw_line((bounding_box.x1, bounding_box.y1), (0,0))
        #shape.finish(color=(0,0,1))
        #shape.commit()

        page.set_cropbox(bounding_box)
        #print(page.show_pdf_page)

        #dx = bounding_box.x0 - A4Width/2 + (bounding_box.x1 - bounding_box.x0)/2
        #dy = 0#bounding_box.y1# - A4Height/2 + (bounding_box.y1 - bounding_box.y0)/2
        #paper = pymupdf.Rect(dx, dy, dx + A4Width, dy + A4Height)
        #page.set_mediabox(paper)

    doc.save(output_filename)

if __name__ == '__main__':
    main(sys.argv)
