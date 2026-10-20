FROM ubuntu:22.04

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl bzip2 ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Pin a version (check release.anza.xyz / GitHub releases for the one you want)
ARG AGAVE_VERSION=v2.3.4
RUN sh -c "$(curl -sSfL https://release.anza.xyz/${AGAVE_VERSION}/install)"

ENV PATH="/root/.local/share/solana/install/active_release/bin:${PATH}"

WORKDIR /ledger
EXPOSE 8899 8900 9900

ENTRYPOINT ["solana-test-validator", "--bind-address", "0.0.0.0", "--ledger", "/ledger"]
CMD ["--reset"]