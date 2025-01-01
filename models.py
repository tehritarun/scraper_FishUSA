
from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Pagination(BaseModel):
    totalResults: int
    begin: int
    end: int
    currentPage: int
    totalPages: int
    previousPage: int
    nextPage: int
    perPage: int
    defaultPerPage: int


class Result(BaseModel):
    brand: str
    categories_hierarchy: List[str]
    # custom_badge_new: Optional[str] = None
    # custom_category_options_text: str
    # custom_ss_hide: str
    # custom_ss_pricemax: str
    # custom_ss_pricemaxonsale: str
    # custom_ss_pricemin: str
    # custom_ss_priceminonsale: str
    id: str
    imageUrl: str
    # intellisuggestData: str
    # intellisuggestSignature: str
    msrp: str
    name: str
    # option_set_id: str
    popularity: str
    price: str
    product_type_unigram: str
    ratingCount: str
    sku: str
    # ss_custom_badges: str
    # ss_days_since_c_sort_newest: str
    # ss_has_options: str
    # ss_image_hover: Optional[str] = None
    # ss_in_stock: str
    # ss_retail: str
    thumbnailImageUrl: str
    uid: str
    url: str
    ss_price_range: Optional[str] = None
    ss_swatches: Optional[str] = None


class Value(BaseModel):
    active: bool
    type: str
    value: Optional[str] = None
    label: str
    count: int
    low: Optional[str] = None
    high: Optional[str] = None


class Facet(BaseModel):
    field: str
    label: str
    type: str
    multiple: str
    collapse: int
    facet_active: int
    hierarchyDelimiter: Optional[str] = None
    values: List[Value]


class Position(BaseModel):
    index: int


class Config(BaseModel):
    position: Position


class InlineItem(BaseModel):
    value: str
    config: Config


class Content(BaseModel):
    header: List[str]
    inline: List[InlineItem]


class TriggeredCampaign(BaseModel):
    id: str
    title: str
    type: str


class Merchandising(BaseModel):
    redirect: str
    is_elevated: List
    elevated: List
    removed: List
    content: Content
    facets: List
    facetsHide: List
    experiments: List
    variants: List
    personalized: bool
    triggeredCampaigns: List[TriggeredCampaign]


class JSONResponseModel(BaseModel):
    pagination: Optional[Pagination]
    # sorting: Sorting
    # resultLayout: str
    results: Optional[List[Result]]
    # facets: List[Facet]
    # breadcrumbs: List
    # filterSummary: List
    # merchandising: Merchandising
