import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from '@/shared/ui'

import { createPages } from '../lib'

interface PaginationProps {
  count: number
  page: number
  onChange: (page: number) => void
}

export const ControlledPagination = ({
  count,
  page,
  onChange,
}: PaginationProps) => {
  if (count <= 1) return null

  const currentPage = Math.max(1, Math.min(page, count))
  const pages = createPages(currentPage, count)
  return (
    <Pagination>
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious
            onClick={() => onChange(currentPage - 1)}
            disabled={currentPage === 1}
          />
        </PaginationItem>
        {pages.map((p, index) => (
          <PaginationItem key={index}>
            {p === 'ellipsis' ? (
              <PaginationEllipsis />
            ) : (
              <PaginationLink
                isActive={p === currentPage}
                onClick={() => onChange(p as number)}
                aria-label={`Go to page ${p}`}
                disabled={p === currentPage}
              >
                {p}
              </PaginationLink>
            )}
          </PaginationItem>
        ))}
        <PaginationItem>
          <PaginationNext
            onClick={() => onChange(currentPage + 1)}
            disabled={currentPage === count}
          />
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  )
}
