from typing import Optional, List
from pydantic import BaseModel, Field

class PeopleSearchQuery(BaseModel):
    person_titles: Optional[List[str]] = Field(default=None, description="Job titles held by the people you want to find. For a person to be included in search results, they only need to match 1 of the job titles you add. Adding more job titles expands your search results. Results also include job titles with the same terms, even if they are not exact matches. For example, searching for `marketing manager` might return people with the job title `content marketing manager`. Use this parameter in combination with the `person_seniorities[]` parameter to find people based on specific job functions and seniority levels. Examples: `sales development representative`; `marketing manager`; `research analyst`")
    include_similar_titles: Optional[bool] = Field(default=True, description="This parameter determines whether people with job titles similar to the titles you define in the `person_titles[]` parameter are returned in the response. Set this parameter to `false` when using `person_titles[]` to return only strict matches for job titles.")
    person_locations: Optional[List[str]] = Field(default=None, description="The location where people live. You can search across cities, US states, and countries. To find people based on the headquarters locations of their current employer, use the `organization_locations` parameter. Examples: `california`; `ireland`; `chicago`")
    person_seniorities: Optional[List[str]] = Field(default=None, description="The job seniority that people hold within their current employer. This enables you to find people that currently hold positions at certain reporting levels, such as Director level or senior IC level. For a person to be included in search results, they only need to match 1 of the seniorities you add. Adding more seniorities expands your search results. Searches only return results based on their current job title, so searching for Director-level employees only returns people that currently hold a Director-level title. If someone was previously a Director, but is currently a VP, they would not be included in your search results. Use this parameter in combination with the `person_titles[]` parameter to find people based on specific job functions and seniority levels. The following options can be used for this parameter: `owner`, `founder`, `c_suite`, `partner`, `vp`, `head`, `director`, `manager`, `senior`, `entry`, `intern`")
    organization_locations: Optional[List[str]] = Field(default=None, description="The location of the company headquarters for a person's current employer. You can search across cities, US states, and countries. If a company has several office locations, results are still based on the headquarters location. For example, if you search `chicago` but a company's HQ location is in `boston`, people that work for the Boston-based company will not appear in your results, even if they match other parameters. To find people based on their personal location, use the `person_locations` parameter. Examples: `texas`; `tokyo`; `spain`")
    q_organization_domains_list: Optional[List[str]] = Field(default=None, description="The domain name for the person's employer. This can be the current employer or a previous employer. Do not include `www.`, the `@` symbol, or similar. This parameter accepts up to 1,000 domains in a single request. Examples: `apollo.io`; `microsoft.com`")
    contact_email_status: Optional[List[str]] = Field(default=None, description="The email statuses for the people you want to find. You can add multiple statuses to expand your search. The statuses you can search include: `verified`, `unverified`, `likely to engage`, `unavailable`")
    organization_ids: Optional[List[str]] = Field(default=None, description="The Apollo IDs for the companies (employers) you want to include in your search results. Each company in the Apollo database is assigned a unique ID. To find IDs, call the [Organization Search endpoint](/reference/organization-search) and identify the values for `organization_id`. Example: `5e66b6381e05b4008c8331b8`")
    organization_num_employees_ranges: Optional[List[str]] = Field(default=None, description="The number range of employees working for the person's current company. This enables you to find people based on the headcount of their employer. You can add multiple ranges to expand your search results. Each range you add needs to be a string, with the upper and lower numbers of the range separated only by a comma. Examples: `1,10`; `250,500`; `10000,20000`")
    q_keywords: Optional[str] = Field(default=None, description="A string of words over which we want to filter the results.")
    page: Optional[int] = Field(default=None, description="The page number of the Apollo data that you want to retrieve. Use this parameter in combination with the `per_page` parameter to make search results for navigable and improve the performance of the endpoint. Example: `4`")
    per_page: Optional[int] = Field(default=None, description="The number of search results that should be returned for each page. Limited the number of results per page improves the endpoint's performance. Use the `page` parameter to search the different pages of data. Example: `10`")

class ApiSearchOrganization(BaseModel):
    """Organization summary in People API Search results (no PII)."""
    name: str = Field(description="Organization name")
    has_industry: Optional[bool] = Field(default=None, description="Whether industry data is available")
    has_phone: Optional[bool] = Field(default=None, description="Whether phone is available")
    has_city: Optional[bool] = Field(default=None, description="Whether city is available")
    has_state: Optional[bool] = Field(default=None, description="Whether state is available")
    has_country: Optional[bool] = Field(default=None, description="Whether country is available")
    has_zip_code: Optional[bool] = Field(default=None, description="Whether zip code is available")
    has_revenue: Optional[bool] = Field(default=None, description="Whether revenue data is available")
    has_employee_count: Optional[bool] = Field(default=None, description="Whether employee count is available")


class ApiSearchPerson(BaseModel):
    """Person record from People API Search (no email/phone; use Enrichment to get contact details)."""
    id: str = Field(description="Apollo person ID")
    first_name: str = Field(description="First name")
    last_name_obfuscated: Optional[str] = Field(default=None, description="Obfuscated last name e.g. Hu***n")
    title: Optional[str] = Field(default=None, description="Job title")
    last_refreshed_at: Optional[str] = Field(default=None, description="When the record was last refreshed")
    has_email: Optional[bool] = Field(default=None, description="Whether email is available (enrich to get it)")
    has_city: Optional[bool] = Field(default=None, description="Whether city is available")
    has_state: Optional[bool] = Field(default=None, description="Whether state is available")
    has_country: Optional[bool] = Field(default=None, description="Whether country is available")
    has_direct_phone: Optional[str] = Field(default=None, description="e.g. 'Yes' if direct phone is available")
    organization: Optional[ApiSearchOrganization] = Field(default=None, description="Current employer summary")


class PeopleSearchResponse(BaseModel):
    """Response from People API Search (mixed_people/api_search). Does not include emails or phone numbers."""
    total_entries: int = Field(description="Total number of people matching the search")
    people: List[ApiSearchPerson] = Field(default_factory=list, description="Page of people results")
