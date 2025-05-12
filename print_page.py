import sys
import pymupdf

A4Paper = pymupdf.Rect(0, 0, 595, 842)

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

    # Check for empty page
    if not rects:
        return None

    # Merge bounding boxes
    bounding_box = rects[0]
    for rect in rects[1:]:
        bounding_box |= rect

    return bounding_box

def make_print_page(srcpage, srcpage_rect, dstpage, dstpage_rect):

    x_margin = (dstpage_rect.width - srcpage_rect.width)/2
    y_margin = (dstpage_rect.height - srcpage_rect.height)/2

    dstrect = pymupdf.Rect(dstpage_rect.x0 + x_margin, dstpage_rect.y0 + y_margin,
                           dstpage_rect.x1 - x_margin, dstpage_rect.y1 - y_margin)
    dstpage.show_pdf_page(dstrect, srcpage.parent, srcpage.number, clip=srcpage_rect, keep_proportion=False)

    print(f'{srcpage_rect} -> {dstpage_rect}')

    m = 5 # margin

    shape = dstpage.new_shape()
    shape.draw_line((dstrect.x0, dstrect.y0-m), (dstrect.x0, 0))
    shape.draw_line((dstrect.x0-m, dstrect.y0), (dstpage_rect.x0, dstrect.y0))

    shape.draw_line((dstrect.x1, dstrect.y0-m), (dstrect.x1, 0))
    shape.draw_line((dstrect.x1+m, dstrect.y0), (dstpage_rect.x1, dstrect.y0))

    shape.draw_line((dstrect.x0, dstrect.y1+m), (dstrect.x0, dstpage_rect.height))
    shape.draw_line((dstrect.x0-m, dstrect.y1), (dstpage_rect.x0, dstrect.y1))

    shape.draw_line((dstrect.x1, dstrect.y1+m), (dstrect.x1, dstpage_rect.y1))
    shape.draw_line((dstrect.x1+m, dstrect.y1), (dstpage_rect.x1, dstrect.y1))

    shape.finish(color=(0,0,0))
    shape.commit()

def main(argv):
    input_filename = argv[1]
    output_filename = argv[2]
    src = pymupdf.open(input_filename)
    dst = pymupdf.open()

    rects = [page_bounding_box(page) for page in src]

    bounding_box = rects[0]
    for rect in rects[1:]:
        bounding_box |= rect

    for srcpage in src:
        dstpage = dst.new_page()
        columns = 2
        width = A4Paper.width/columns
        for column in range(columns):
            rect = pymupdf.Rect(column*width, 0, (column+1)*width, A4Paper.height)
            make_print_page(srcpage, bounding_box, dstpage, rect)

    dst.save(output_filename, garbage=4, deflate=True)

if __name__ == '__main__':
    main(sys.argv)
