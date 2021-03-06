from typing import Any, Dict, List
from pandas import DataFrame
from lib.pipeline import DefaultPipeline


class SourceNamePipeline(DefaultPipeline):
    """ This is a custom pipeline that downloads a CSV file and outputs it as-is """

    data_urls: List[str] = ["http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv"]
    """ Define our data URLs, which can be more than one """

    fetch_opts: List[Dict[str, Any]] = []
    """ Leave the fetch options as the default, see [lib.net.download] for more details """

    def parse_dataframes(
        self, dataframes: List[DataFrame], aux: Dict[str, DataFrame], **parse_opts
    ) -> DataFrame:
        """
        If the data fetched uses a supported format, (XLS, CSV or JSON), it will be automatically
        parsed and passed as an argument to this function. For data that requires special parsing,
        override the [DefaultPipeline.parse] function instead.
        """

        # We only fetched one source, so the list will be of length one
        data = dataframes[0]

        # Here we can manipulate the data any way we want...

        # The default merge strategy is defined in [DefaultPipeline.merge], see that method for
        # more details. Whenever possible, add a 'key' column to each record with a value found in
        # aux['metadata']['key'] for the best performance.
        # data['key'] = ...

        # Finally, return the data which is ready to go to the next step of the pipeline
        return data

    ##
    # Any functions of DefaultPipeline could be overridden here. We could also
    # define our own functions to the class if necessary.
    ##
