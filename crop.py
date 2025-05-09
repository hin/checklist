import sys
import pymupdf

A4Width = 595
A4Height = 842

a4rect = pymupdf.Rect(0, 0, A4Width, A4Height)

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
    src = pymupdf.open(input_filename)
    dst = pymupdf.open()

    rects = [page_bounding_box(page) for page in src]

    bounding_box = rects[0]
    for rect in rects[1:]:
        bounding_box |= rect

    print(bounding_box)

    for page in src:
        #shape = page.new_shape()
        #shape.draw_rect(bounding_box)
        #shape.finish(color=(1,0,0))
        #shape.draw_line((bounding_box.x1, bounding_box.y1), (0,0))
        #shape.finish(color=(0,0,1))
        #shape.commit()

        #page.set_cropbox(bounding_box)

        w = page.rect.x1 - page.rect.x0
        h = page.rect.y1 - page.rect.y0

        x = (A4Width - w)/2
        y = (A4Height - h)/2

        newpage = dst.new_page()
        dstrect = pymupdf.Rect(x,y,x+w,y+h)
        newpage.show_pdf_page(dstrect, src, page.number)

        m = 10 # margin

        shape = newpage.new_shape()
        shape.draw_line((dstrect.x0, dstrect.y0-m), (dstrect.x0, 0))
        shape.draw_line((dstrect.x0-m, dstrect.y0), (0, dstrect.y0))

        shape.draw_line((dstrect.x1, dstrect.y0-m), (dstrect.x1, 0))
        shape.draw_line((dstrect.x1+m, dstrect.y0), (A4Width, dstrect.y0))

        shape.draw_line((dstrect.x0, dstrect.y1+m), (dstrect.x0, A4Height))
        shape.draw_line((dstrect.x0-m, dstrect.y1), (0, dstrect.y1))

        shape.draw_line((dstrect.x1, dstrect.y1+m), (dstrect.x1, A4Height))
        shape.draw_line((dstrect.x1+m, dstrect.y1), (A4Width, dstrect.y1))

        shape.finish(color=(0,0,0))
        shape.commit()
    
    dst.save(output_filename, garbage=4, deflate=True)

if __name__ == '__main__':
    main(sys.argv)
