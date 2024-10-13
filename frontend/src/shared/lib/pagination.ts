const SIBLING_COUNT = 1
const BOUNDARY_COUNT = 1

export const createPages = (
  currentPage: number,
  count: number
): (number | 'ellipsis')[] => {
  const totalPageNumbers = SIBLING_COUNT * 2 + BOUNDARY_COUNT * 2 + 3
  const pages: Array<number | 'ellipsis'> = []

  if (count <= totalPageNumbers) {
    for (let i = 1; i <= count; i++) {
      pages.push(i)
    }
  } else {
    const leftSiblingIndex = Math.max(
      currentPage - SIBLING_COUNT,
      BOUNDARY_COUNT + 2
    )
    const rightSiblingIndex = Math.min(
      currentPage + SIBLING_COUNT,
      count - BOUNDARY_COUNT - 1
    )
    const showLeftEllipsis = leftSiblingIndex > BOUNDARY_COUNT + 2
    const showRightEllipsis = rightSiblingIndex < count - BOUNDARY_COUNT - 1

    for (let i = 1; i <= BOUNDARY_COUNT; i++) {
      pages.push(i)
    }

    if (showLeftEllipsis) {
      pages.push('ellipsis')
    } else {
      for (let i = BOUNDARY_COUNT + 1; i < leftSiblingIndex; i++) {
        pages.push(i)
      }
    }

    for (let i = leftSiblingIndex; i <= rightSiblingIndex; i++) {
      pages.push(i)
    }

    if (showRightEllipsis) {
      pages.push('ellipsis')
    } else {
      for (let i = rightSiblingIndex + 1; i < count - BOUNDARY_COUNT + 1; i++) {
        pages.push(i)
      }
    }

    for (let i = count - BOUNDARY_COUNT + 1; i <= count; i++) {
      pages.push(i)
    }
  }

  return pages
}
